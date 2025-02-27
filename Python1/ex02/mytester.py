from load_image import ft_load
print("Test with JPG and JPEG images\n")
print(ft_load("landscape.jpg"))
print("\n-------------------------------\n")
print(ft_load("animal.jpeg"))
print("\n-------------------------------\n")
print("Test with wrong file\n")
print(ft_load("wrong_file.jpg"))
