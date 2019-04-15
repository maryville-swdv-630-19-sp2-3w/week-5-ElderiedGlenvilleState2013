#Elderied McKinney week 5 home work

from abc import ABCMeta, abstractmethod
import copy


#creating customer reward system using factory
class Customer(metaclass=ABCMeta):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
    @abstractmethod
    def get_rewardAccount(self):
        
        pass
    
    def __str__(self):
        return "{} - {}, {} years {}".format(self.__class__. __name__ , self.name, self.age, self.gender)
    
        
        
        
        
        
        
class GoldMember(Customer):
    def get_rewardAccount(self):
        return "gold"
    
    
    
    
class PlusMember(Customer):
    def get_rewardAccount(self):
        return "plus"
    
    
class PrimeMember(Customer):
    def get_rewardAccount(self):
        return "prime"
    
    
    
    
class CustomerFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == 'gold':
            return GoldMember(*args)
        elif name == 'plus':
            return PlusMember(*args)
        elif name == 'prime':
            return PrimeMember(*args)
        
        
        
        
def main2():
    customer = CustomerFactory()
    print (customer.create('gold', 'Bam', 25, 'M'))
    print (CustomerFactory.create('prime', 'Gracy', 28, 'F')) #better

    prime = customer.create('prime', 'Thema', 39, 'F')
    print(prime)

    plus = customer.create('plus', 'Supritha', 32, 'F')
    print(plus.get_rewardAccount())
    
    
    
    
main2()
  
 
#Proxy design

class RewardProxy(object):
    count = 0
    
    def __new__(cls, *args):
        
        instance = object.__new__(cls)
        cls.increase_count()
        return instance
    
    def __init__(self, customer):
        self.customer = customer
        
    @classmethod
    def increase_count(cls):
        cls.count += 1
        
    @classmethod     
    def decrease_count(cls):
        cls.count -= 1
        
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    def __str__(self):
        return str(self.customer)
    
    def __getattr__(self, name):
        return getattr(self.customer, name)
    
    def __del__(self):
        self.decrease_count()
        
        
        
        
        
class CustomerProxyFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == 'gold':
            return RewardProxy(GoldMember(*args))
        elif name == 'plus':
            return RewardProxy(PlusMember(*args))
        elif name == 'prime':
            return RewardProxy(PrimeMember(*args))

    
        
        
def main2():
    plusMember = CustomerProxyFactory.create('plus', 'John', 33, 'M')
    print(plusMember)
    
    goldMember = CustomerProxyFactory.create('gold', 'Mary', 18, 'F')
    print(goldMember.get_count())
    print(RewardProxy.get_count())
    
    del plusMember
    print(RewardProxy.get_count())
    
    
    
    
main2() 
    
    
#buider

import abc

# represents the product created by the builder.
class Pizza:
    def __init__(self):
        self.topping = None

    def get_toping(self):
        return self.topping

    def set_topping(self, topping):
        self.topping = topping

    def __str__(self):
        return "Toppings [topping={0}]".format(self.topping)


# the builder abstraction
class PizzaBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_topping(self, topping):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass


class PizzaBuilderDeepdish(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_topping(self, topping):
        self.pizza.set_topping(topping)

    def get_result(self):
        return self.pizza


class PizzaBuildDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_topping("cheese");
        return self.builder.get_result()

def main3():
    builder = PizzaBuilderDeepdish()
    pizzabuildDirector = PizzaBuildDirector(builder)
    print(pizzabuildDirector.construct())
    
    
    
    
main3()    
    