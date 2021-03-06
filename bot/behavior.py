#!/usr/bin/python -tt

#from settings import MODULES

MODULES = ['irc']

import os
import re

# Global variables

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'


# Helper functions

def regexify(data):
    matchObj = re.match(regex, data, re.M|re.I)
    if matchObj:
        return matchObj.group(), matchObj.group(1), matchObj.group(2),\
                matchObj.group(3), matchObj.group(4), matchObj.group(5),\
                matchObj.group(6)
    else:
        return ''



def get_nick(string):
    return string[0:string.index('!')]



def list_modules():
    string = ' '

    if len(MODULES) == 1:
        return 'We have 1 module : ' + str(MODULES[0])
    else:
        count = 1
        for e in MODULES:
            string += str(e) + ', '
        return 'We have '+str(len(MODULES))+' modules : '+ str(string[:-2])



def get_module(string):
    return string[string.index('!') + 6:][:-1]


def get_chapters(module):
    path = '.'
    chapters = []
    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith((".txt")):
                matchObj = re.match('./(\S+)/(\S+)', situated_at, re.M|re.I)
                if module in MODULES:
                    if module == matchObj.group(2):
                        chapters.append(file_name)
                    else:
                        pass
                else:
                    pass

    return chapters



# AI Functions

def ai(data, bot, irc):
    bot_type, nick, ident, password, channel, realname, hostname = bot

    if data.find('PING') != -1:
        irc.send('PONG ' + data.split() [1] + '\r\n')

    if data.find('Message of the Day') != -1:
        irc.send('JOIN ' + str(channel) + '\r\n')

    if data.find('+iwR') != -1:
        irc.send('PRIVMSG NickServ IDENTIFY ' + str(nick) + ' ' + str(password) + '\r\n')

    if data.find('KICK') != -1:
        irc.send('JOIN ' + str(channel) + '\r\n')

    if bot_type == 'Helper':
        regexed_list = []

        if data.find('PRIVMSG '+ nick + ' :!tutor') != -1:
            regexed_list = regexify(data)
            msgto = get_nick(regexed_list[2])
            string = list_modules()
            irc.send('PRIVMSG ' + str(msgto) + ' :Hi ' + msgto +' ! \r\n')
            irc.send('PRIVMSG ' + str(msgto) + ' :What would you like to learn ?\r\n')
            irc.send('PRIVMSG ' + str(msgto) + ' :You can learn : \r\n')
            irc.send('PRIVMSG ' + str(msgto) + ' :'+ string + '\r\n')
            irc.send('PRIVMSG ' + str(msgto) + ' :List the chapters using !list <modulename>\r\n')

        if data.find('PRIVMSG '+ nick + ' :!list') != -1:
            regexed_list = regexify(data)
            msgto = get_nick(regexed_list[2])
            module = get_module(regexed_list[6])
            irc.send('PRIVMSG ' + str(msgto) + ' :Module '+ str(module) +' has the following chapters : \r\n')


    if bot_type == 'Teacher':
        pass

