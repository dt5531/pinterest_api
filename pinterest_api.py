from config import *
from constant import *
from helper import *

import requests as req
import time

class Pinterest(object):
    def __init__(self):
        self.token = ACCESS_TOKEN
###############################################################################
#                                   Users                                     #
###############################################################################

#####################
#  Fetch User Data  #
#####################

    # get current user
    def get_current_user(self):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + ME
        return req.get(request_link, params=payload)

    # get current user's board
    def get_current_user_board(self):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + ME + BOARD
        return req.get(request_link, params=payload)

    # get user's suggestion with pinid
    def get_suggested_with_pin(self, pin_id):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field, PINID: pin_id}
        request_link = PINTEREST_URL + ME + BOARD + SUGGEST
        return req.get(request_link, params=payload)

    # get user's likes
    def get_user_likes(self, cursor=None):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + LIKE
        return req.get(request_link, params=payload)

    # get current user's pins
    def get_current_user_pin(self, cursor=None):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + PIN
        return req.get(request_link, params=payload)

######################
#  Search User Data  #
######################

    # Search current user's board with query
    def query_user_board(self, query, cursor=None):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field, CURSOR: cursor, QUERY: query}
        request_link = PINTEREST_URL + ME + SEARCH + BOARD
        return req.get(request_link, params=payload)

    # Search current user's pins with query
    def query_user_pins(self, query, cursor=None):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field, CURSOR: cursor, QUERY: query}
        request_link = PINTEREST_URL + ME + SEARCH + PIN
        return req.get(request_link, params=payload)

########################
#  Create Follow Data  #
########################

    # get user to follow a specific board given username and board name
    def follow_board(self, username, board_name):
        board = get_board_name(username, board_name)
        data = {BOARD_DATA: board}
        payload = {TOKEN: self.token}
        request_link = PINTEREST_URL + ME + FOLLOW + BOARD
        return req.post(request_link, params=payload, data=data)

    # get user to follow a specific user given username
    def follow_user(self, username):
        data = {USER_DATA: username}
        payload = {TOKEN: self.token}
        request_link = PINTEREST_URL + ME + FOLLOW + USER
        return req.post(request_link, params=payload, data=data)

#######################
#  Fetch Follow Data  #
#######################

    # get user's current followers
    def get_user_follower(self, cursor=None):
        payload = {TOKEN: self.token, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + FOLLOWER
        return req.get(request_link, params=payload)

    # get user's following board
    def get_user_follow_board(self, cursor=None):
        payload = {TOKEN: self.token, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + FOLLOW + BOARD
        return req.get(request_link, params=payload)

    def get_user_interest(self, cursor=None):
        payload = {TOKEN: self.token, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + FOLLOW + INTEREST
        return req.get(request_link, params=payload)

    def get_user_following(self, cursor=None):
        payload = {TOKEN: self.token, CURSOR: cursor}
        request_link = PINTEREST_URL + ME + FOLLOW + USER
        return req.get(request_link, params=payload)

#######################
#  Fetch Follow Data  #
#######################

    # unfollow a specific board
    def unfollow_board(self, username, board_name):
        board = get_board_name(username, board_name) + "/"
        payload = {TOKEN: self.token}
        request_link = PINTEREST_URL + ME + FOLLOW + BOARD + board
        return req.delete(request_link, params=payload)

    # unfollow a speecific user
    def unfollow_user(self, username):
        payload = {TOKEN: self.token}
        request_link = PINTEREST_URL + ME + FOLLOW + USER + username + "/"
        return req.delete(request_link, params=payload)

###############################################################################
#                                  Boards                                     #
###############################################################################

###################
#  Create Boards  #
###################

    # Create a board for current user
    def create_board(self, name, description=None):
        field = get_fields()
        data = {NAME: name, DESCRIPTION: description}
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + BOARD
        return req.post(request_link, params=payload, data=data)

######################
#  Fetch Board Data  #
######################

    # retreive board info given board name
    def get_board(self, username, board_name):
        board = get_board_name(username, board_name) + "/"
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + BOARD + board
        return req.get(request_link, params=payload)

    # current only get pins from fall-2016-runaway board
    def get_board_pin(self, username, board_name, cursor=None):
        board = get_board_name(username, board_name) + "/"
        field = get_fields(_id=True)
        payload = {TOKEN: self.token, FIELDS: field, CURSOR: cursor}
        request_link = PINTEREST_URL + BOARD + board + PIN
        return req.get(request_link, params=payload)

#####################
#  Edit Board Data  #
#####################

    def edit_user_board(self, username, board_name, name=None, description=None):
        board = get_board_name(username, board_name)
        data = {BOARD_DATA: board, NAME: name, DESCRIPTION: description}
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + BOARD + board + "/"
        return req.patch(request_link, params=payload, data=data)

###################
#  Delete Boards  #
###################

    def remove_board(self, username, board_name):
        board = get_board_name(username, board_name)
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + BOARD + board + "/"
        return req.delete(request_link, params=payload)

###############################################################################
#                                   Pins                                      #
###############################################################################

#################
#  Create Pins  #
#################

    # Create pin for a specific board
    def post_pin(self, username, board_name, note, link=None,
            image_url=None, image=None, image_base64=None):
        if image_url == None and image == None and image_base64 == None:
            return "Image needed"

        board = get_board_name(username, board_name)
        data = {
                BOARD_DATA: board, NOTE: note, LINK: link,
                IMAGE_URL: image_url, IMAGE: image, IMAGE64: image_base64
                }
        request_link = PINTEREST_URL + PIN
        payload = {TOKEN: self.token}
        return req.post(request_link, params=payload, data=data)

################
#  Fetch Pins  #
################

    # retreive post info given pin id
    def get_pin(self, pin_id):
        field = get_fields(_note=True, _image=True, _attribution=True)
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + PIN + pin_id + "/"
        return req.get(request_link, params=payload)

################
#  Patch Pins  #
################

    def edit_pin(self, pin_id, username=None, board_name=None, note=None, link=None):
        if username != None and board_name != None:
            board = get_board_name(username, board_name)
        elif username == None and board_name == None:
            board = None
        else:
            return "Need proper board name"
        field = get_fields()
        data = {PINID: pin_id, }
        payload = {TOKEN: self.token, FIELDS: field,
                BOARD_DATA: board, NOTE: note, LINK: link}
        request_link = PINTEREST_URL + PIN + pin_id + "/"
        return req.patch(request_link, params=payload, data=data)

#################
#  Delete Pins  #
#################

    def remove_pin(self, pin_id):
        payload = {TOKEN: self.token}
        request_link = PINTEREST_URL + PIN + pin_id + "/"
        return req.delete(request_link, params=payload)

###############################################################################
#                                   Extras                                    #
###############################################################################

    # get user given specific username
    def get_user(self, username):
        field = get_fields()
        payload = {TOKEN: self.token, FIELDS: field}
        request_link = PINTEREST_URL + USER + username + "/"
        return req.get(request_link, params=payload)

if __name__ == "__main__":
    p = Pinterest()
    user_info = p.get_current_user()
    print (user_info.json())
