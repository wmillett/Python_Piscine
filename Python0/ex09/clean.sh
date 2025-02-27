if [ -d "./ft_package/dist" ]; then
    rm -rf ./ft_package/dist
    echo "Removed the ft_package/dist directory."
fi

if [ -d "./ft_package/ft_package.egg-info" ]; then
    rm -rf ./ft_package/ft_package.egg-info
    echo "Removed the ft_package.egg-info directory."
fi

if pip freeze | grep -q ft_package ; then
    pip uninstall -y ft_package > /dev/null 2>&1
    echo "Uninstalled the ft_package."
fi

if pip freeze | grep -q UNKNOWN ; then
    pip uninstall -y UNKNOWN > /dev/null 2>&1
    echo "Uninstalled the UNKNOWN package."
fi

echo "Cleaned the ft_package."