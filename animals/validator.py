class DataValidationError(Exception):
    ...

class ValidateCamps():
    def verify_camps(validated_data):
        if(validated_data.traits ):
            return {'field': 'traits', 'is_valid':False}

        if(validated_data.group):
            return {'field': 'group', 'is_valid':False}
            
        if(validated_data.sex):
            return {'field': 'sex', 'is_valid':False}


        return True

class AnimalValidator:
    valid_keys = [
        "name",
        "age",
        "weight",
        "group",
        "traits",

    ]

    valid_inputs = {
        "name": str,
        "age": int,
        "weight": float,
        "group": object,
        "traits": list    
    }

    def __init__(self, *args: tuple, **kwargs: dict):
        self.data = kwargs
        self.errors = {}

    def is_valid(self) -> bool:
        try:
            self.validate_required_keys()

            return True
        except(KeyError, DataValidationError):
            return False

    def valid_update(self, data_request):
        try:
            self.validate_camps(data=data_request)

            return True
        except(DataValidationError):
            return False

    def validate_required_keys(self):
        for valid_key in self.valid_keys:
            print('key:',valid_key)
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "[This field is required.]"

        if self.errors:
            raise KeyError

    
    def validate_camps(self, data):
        for type_data in data:
            if type_data == "sex" or type_data == 'group' or type_data == 'traits':
                self.errors[type_data] = f'You can not update {type_data} property.'

        if self.errors:
            raise DataValidationError