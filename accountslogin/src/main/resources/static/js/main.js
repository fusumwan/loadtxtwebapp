/**************************************************
 * Course: Web and Database Computing (2207)
 * 2019 Group Project
 * Author: Sum Wan, FU
 * Date: 7-5-2019
 * Student ID: 1714470
 * Description: Main JavaScript
 **************************************************/

let headNavOpened = false;

document.addEventListener('DOMContentLoaded', () => {
  const handleResize = () => {
    const width = window.innerWidth;
    const navUl = document.querySelector('.head-nav ul');
    if (width > 768) {
      navUl.style.display = 'block';
    } else {
      navUl.style.display = headNavOpened ? 'block' : 'none';
    }
  };

  window.addEventListener('resize', handleResize);
  handleResize();

  const menu = document.querySelector('span.menu');
  if (menu) {
    menu.addEventListener('click', () => {
      const navUl = document.querySelector('.head-nav ul');
      navUl.style.display = (navUl.style.display === 'none' || !navUl.style.display) ? 'block' : 'none';
      headNavOpened = !headNavOpened;
    });
  }
});
