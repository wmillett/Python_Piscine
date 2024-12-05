ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "world"

ft_tuple = (ft_tuple[0], "Germany")

ft_set = list(ft_set)
ft_set[0] = "Hello"
ft_set[1] = "Berlin"

ft_dict["Hello"] = "42Berlin"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)