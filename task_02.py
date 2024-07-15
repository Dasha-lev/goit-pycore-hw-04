def get_cats_info(path):

   
    cats_info = []
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Split the line into id, name and age 
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_id, cat_name, cat_age = cat_data
                    # Create a dictionary for cats
                    cat_dict = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": int(cat_age)
                    }
                    # Add dictionary to the list
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Error: The file at path {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
