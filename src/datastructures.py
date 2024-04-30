
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure():
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = [
            {
                                "id": self._generate_id(),
                                "first_name": "John",
                                "last_name": last_name,
                                "age": 33,
                                "lucky_numbers": [7, 13, 22]
                            },
                            {
                                "id": self._generate_id(),
                                "first_name": "Jane",
                                "last_name": last_name,
                                "age": 35,
                                "lucky_numbers": [10, 14, 3]
                            },
                            {
                                "id": self._generate_id(),
                                "first_name": "Jimmy",
                                "last_name": last_name,
                                "age": 5,
                                "lucky_numbers": [1]
                            }
        ]
                            

    # read-only: Use this method to generate random members ID's when adding members into the list

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        return self._members.append(member)
        ## Agrega un nuevo miembro a la lista de _members
        pass

    def delete_member(self, id):
        ## Debes implementar este método
        for item in self._members:
            if item['id'] == id:
                self._members.remove(item)
            break
        ## Recorre la lista y elimina el miembro con el id proporcionado
        pass

    def get_member(self, id):
        ## Debes implementar este método
        for item in self._members:
            if item['id'] == id:
                return item
            break
        return False
        ## Recorre la lista y obtén el miembro con el id proporcionado
        pass

    def get_all_members(self):
        return self._members
