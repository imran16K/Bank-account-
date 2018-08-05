from abc import ABCMeta, abstractmethod
from random import random

#using classes by force using meta classes

class Account(metaclass=ABCMeta):

    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0





