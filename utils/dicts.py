def get_val(collection, key, default='git'):
    return_data = collection.get(key)
    if return_data is not None:
        return return_data
    return default
