
dule that supplies Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Definition of the Review class
    '''
    place_id = ""
    user_id = ""
    text = ""
