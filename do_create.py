def do_create(self, args):
    """ Create an object of any class"""
    tokens = args.split()

    # extract class name and params
    class_name = tokens[0]

    params = tokens[1:]
    if not args:
        print("** class name missing **")
        return
    elif class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return
    # getting new instance object
    new_instance = HBNBCommand.classes[class_name]()

    for param in params:
        try:
            # splitting each params items to key and values
            k, v = param.split("=")
            # relacing the undescore with whitespace
            v = v.replace("_", " ")
            v = v.replace('"', '\\')
            if v[0] == '"' and v[-1] == '"' and len(v) > 1:
                # extract what i need
                v = v[1:-1]
            # if the value contains .
            if "." in v:
                # convert to a float
                v = float(v)
            else:
                # convert to an integer
                v = int(v)
            setattr(new_instance, k, v)

        except ValueError:
            continue
    storage.save()
    print(new_instance.id)
    storage.save()


def delete(self, obj=None):
    if obj:
        # get key
        key = f"{type(obj).__name__}.{obj.id}"
        del self.__objects[key]


def all(self, cls=None):

    new_dict = {}
    data_dict = self.__objects
    if cls:
        for key in data_dict.keys():
            key_dot_stripped = key.replace('.', ' ')
            key_split = key_dot_stripped.split()

            if (cls.___name__ == key_split[0])

        """Returns a dictionary of models currently in storage"""
    return FileStorage.__objects
