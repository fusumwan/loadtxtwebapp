/**************************************************
 // Author: Sum Wan,FU
 // Date: 27-5-2019
 // Description: Index javascript
 **************************************************/

window.addEventListener("load", function(){
    document.getElementById("home_li").className="active";

    //-- script-for-txt-file-loader --
    var fileInput = document.getElementById("txt_file_input");
    var loadBtn = document.getElementById("load_txt_btn");
    var fileNameEl = document.getElementById("txt_file_name");
    var contentEl = document.getElementById("txt_content");

    // contextPath is defined globally in header.html (may be empty string).
    var basePath = (typeof contextPath !== "undefined" && contextPath) ? contextPath : "";
    var UPLOAD_URL = basePath + "/index/upload_txt/";
    var LOAD_URL = basePath + "/index/load_txt/";

    function setStatus(message){
        if (fileNameEl) { fileNameEl.textContent = message; }
    }

    // Split raw text into an array of paragraphs (blocks separated by one or more blank lines).
    function splitIntoParagraphs(text){
        var normalized = String(text).replace(/\r\n/g, "\n").replace(/\r/g, "\n");
        var blocks = normalized.split(/\n[ \t]*\n+/); // blank line(s) separate paragraphs
        var paragraphs = [];
        for (var i = 0; i < blocks.length; i++) {
            var block = blocks[i].replace(/^\n+|\n+$/g, "").trim();
            if (block.length > 0) {
                paragraphs.push(block);
            }
        }
        return paragraphs;
    }

    function renderTextContent(text){
        var paragraphs = splitIntoParagraphs(text);

        // Rebuild the content area: one <div> per paragraph.
        contentEl.innerHTML = "";
        for (var i = 0; i < paragraphs.length; i++) {
            var p = document.createElement("div");
            p.className = "txt-paragraph";
            // Using textContent safely handles special characters (e.g. < > & ")
            // so raw HTML in the file is shown as text, while MathJax still
            // typesets any LaTeX delimiters found within the paragraph.
            p.textContent = paragraphs[i];
            contentEl.appendChild(p);
        }

        if (paragraphs.length === 0) {
            var empty = document.createElement("div");
            empty.className = "txt-paragraph";
            empty.textContent = "(The file is empty.)";
            contentEl.appendChild(empty);
        }

        if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
            if (typeof window.MathJax.typesetClear === "function") {
                window.MathJax.typesetClear([contentEl]);
            }
            window.MathJax.typesetPromise([contentEl]).catch(function(err){
                console.error("MathJax typeset failed:", err);
            });
        }
    }

    // Step 2: fetch the previously uploaded file's content and render it.
    function loadTxtFromServer(filename){
        setStatus("Loading: " + filename + " ...");
        fetch(LOAD_URL + "?name=" + encodeURIComponent(filename), {
            method: "GET"
        })
        .then(function(response){
            if (!response.ok) { throw new Error("Load failed (HTTP " + response.status + ")"); }
            return response.json();
        })
        .then(function(data){
            setStatus("Loaded: " + data.filename);
            renderTextContent(data.content);
        })
        .catch(function(err){
            console.error(err);
            setStatus("Error loading file: " + err.message);
        });
    }

    // Step 1: upload the selected file to the server (saved under /uploads/txt/).
    function uploadAndLoad(){
        if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
            setStatus("Please choose a .txt file first.");
            return;
        }

        var file = fileInput.files[0];
        var formData = new FormData();
        formData.append("file", file);

        setStatus("Uploading: " + file.name + " ...");
        fetch(UPLOAD_URL, {
            method: "POST",
            body: formData
        })
        .then(function(response){
            if (!response.ok) { throw new Error("Upload failed (HTTP " + response.status + ")"); }
            return response.json();
        })
        .then(function(data){
            // After a successful upload, load the stored file back for display.
            loadTxtFromServer(data.filename);
        })
        .catch(function(err){
            console.error(err);
            setStatus("Error uploading file: " + err.message);
        });
    }

    if (loadBtn) {
        loadBtn.addEventListener("click", function(event){
            event.preventDefault();
            uploadAndLoad();
        });
    }
    //-- script-for-txt-file-loader --
});
