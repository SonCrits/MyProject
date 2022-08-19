from odoo import models, api


#bài tập 1
class ProjectOOP(models.Model):
    _name = 'project.oop'
    _inherit = 'project.project'
    _description = 'Project Object Oriented Programming'
    
    @api.onchange('alias_enabled')
    def _onchange_alias_name(self):
        if not self.alias_enabled:
            self.alias_name = True
            
    def get_name_project(self):
        return self._rec_name
    
            
#bài tập 2
class Abstract(models.AbstractModel):
    _name = 'abstract'
    _description = 'Abstract Model'
    
    def pure_virtual_function(self):
        pass
    
class InheritAbstract(Abstract):
    
    def pure_virtual_function(self):
        print("this is inherit model")
        
        
#bài tập 3       
class Public(models.Model):
    
    name = 'Public'
    
    def getName(self):
        print(self.name)

print(Public().name)
Public.getName()

class InheritPublic(Public):
    pass

#test
InheritPublic().getName() #public

class Prototed(models.Model):
    
    _name = 'Prototed'
    
    def _getName(self):
        print(self._name)
        
print(Prototed()._name) #Prototed
Prototed()._getName() #Prototed

class InheritPrototed(Prototed):
    pass

InheritPrototed()._getName() #Prototed


class Private(models.Model):
    __name = 'Private'
    
    def __getName(self):
        print(self.__name)
        
    def getName(self):
        self.__getName()
        
print(Private().__name) #lỗi no attributes
Private().__getName() #lỗi no attributes
Private.getName() #Private

class InheritPrivate(Private):
    def getNameInPrivate(self):
        self.__getName()
        
#test
InheritPrivate().getNameInPrivate() # lỗi no attributes
    