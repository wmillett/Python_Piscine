if [ -d "./ft_package/dist" ]; then
    rm -rf ./ft_package/dist
    echo "Removed the ft_package/dist directory."
fi
if [ -d "./ft_package/ft_package.egg-info" ]; then
    rm -rf ./ft_package/ft_package.egg-info
    echo "Removed the ft_package.egg-info directory."
fi
echo "Cleaned the ft_package directory."