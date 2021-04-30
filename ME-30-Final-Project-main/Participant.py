import discord
from discord.ext import commands

class Participant:
    def __init__(self, message, points):
        self.user = message.author # discord api
        self.points = points

    def add_points(self,newPoints):
        # based on correct answer from trivia response
        #newPoints = (however you get the data from the other file)
        return self.points += self.newPoints
    
    def __str__(self):
        return "{} has {} points".format(self.user, self.points)