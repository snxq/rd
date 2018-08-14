

def dictsub(obj, fields):
    return {k: v for k,v in obj.items() if k in fields}