echo "Building the ft_package"
cd ft_package
python3 -m build
cd ..
echo "Installing the ft_package method 1"
pip install ./ft_package/dist/ft_package-0.0.1.tar.gz

if [ $? -eq 0 ]; then
    echo "Package installed successfully."
else
    echo "Failed to install the package."
fi

if pip freeze | grep -q ft_package ; then
    pip uninstall -y ft_package > /dev/null 2>&1
    echo "Uninstalled the ft_package."
fi

if pip freeze | grep -q UNKNOWN ; then
    pip uninstall -y UNKNOWN > /dev/null 2>&1
    echo "Uninstalled the UNKNOWN package."
fi

echo "Installing the ft_package method 2"
pip install ./ft_package/dist/ft_package-0.0.1-py3-none-any.whl

if [ $? -eq 0 ]; then
    echo "Package installed successfully."
else
    echo "Failed to install the package."
fi
pip list | grep ft_package
pip show -v ft_package

echo "Running tests on the ft_package"
python3 tester.py
./clean.sh
