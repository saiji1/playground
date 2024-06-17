## with ** pass multiple keywords toa function
def save_user(**user):
    print(user)
    print(user["name"])
    
    
save_user(id=1, name="Saiji", age="22")