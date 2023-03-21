
def insertDataOnTable(fields,model,data):

        print('fields', fields)

        model_obj = model()

        for i in range(len(fields)):

            print('id', data.get(id))

            if fields[i] == 'id':
                continue

            setattr(model_obj, fields[i], data.get(fields[i]))

            print(fields[i], data.get(fields[i]))

        model_obj.save()

        return model_obj