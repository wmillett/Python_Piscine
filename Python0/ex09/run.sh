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

pip list | grep ft_package

echo "Uninstalling the ft_package method 1"
pip uninstall ft_package -y

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
python3 clean.py
