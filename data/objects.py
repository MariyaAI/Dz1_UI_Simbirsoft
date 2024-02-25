from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str
    last_name: str
    post_code: str
    account_number: str = ""
    delete_customer: str = ""
