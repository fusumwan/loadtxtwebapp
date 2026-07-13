from pydantic import BaseModel
from dataclasses import dataclass, field, asdict
from typing import Optional
import json

@dataclass
class Index:
    search_criteria_1: Optional[str] = None
    search_criteria_2: Optional[str] = None
    search_criteria_3: Optional[str] = None

    def get_search_criteria_1(self) -> Optional[str]:
        return self.search_criteria_1

    def set_search_criteria_1(self, value: str):
        self.search_criteria_1 = value

    def get_search_criteria_2(self) -> Optional[str]:
        return self.search_criteria_2

    def set_search_criteria_2(self, value: str):
        self.search_criteria_2 = value

    def get_search_criteria_3(self) -> Optional[str]:
        return self.search_criteria_3

    def set_search_criteria_3(self, value: str):
        self.search_criteria_3 = value

    #use the asdict function from the dataclasses module to convert the dataclass instances to dictionaries. 
    def to_json(self):
        return json.dumps(asdict(self), default=str)
    
    
@dataclass
class Result:
    search_criteria_1: Optional[str] = None
    search_criteria_2: Optional[str] = None
    search_criteria_3: Optional[str] = None

    def get_search_criteria_1(self) -> Optional[str]:
        return self.search_criteria_1

    def set_search_criteria_1(self, value: str):
        self.search_criteria_1 = value

    def get_search_criteria_2(self) -> Optional[str]:
        return self.search_criteria_2

    def set_search_criteria_2(self, value: str):
        self.search_criteria_2 = value

    def get_search_criteria_3(self) -> Optional[str]:
        return self.search_criteria_3

    def set_search_criteria_3(self, value: str):
        self.search_criteria_3 = value
    #use the asdict function from the dataclasses module to convert the dataclass instances to dictionaries. 
    def to_json(self):
        return json.dumps(asdict(self), default=str)
@dataclass
class PageSession:
    index: Optional[Index] = None
    login: Optional[str] = None
    signup: Optional[str] = None
    accountInfo: Optional[str] = None
    result: Optional[Result] = None

    def get_index(self) -> Optional[Index]:
        return self.index

    def set_index(self, value: Index):
        self.index = value

    def get_login(self) -> Optional[str]:
        return self.login

    def set_login(self, value: str):
        self.login = value

    def get_signup(self) -> Optional[str]:
        return self.signup

    def set_signup(self, value: str):
        self.signup = value

    def get_accountInfo(self) -> Optional[str]:
        return self.accountInfo

    def set_accountInfo(self, value: str):
        self.accountInfo = value

    def get_result(self) -> Optional[Result]:
        return self.result

    def set_result(self, value: Result):
        self.result = value
    #use the asdict function from the dataclasses module to convert the dataclass instances to dictionaries. 
    def to_json(self):
        return json.dumps(asdict(self), default=str)