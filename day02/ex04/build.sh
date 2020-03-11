pip3 install --user --upgrade setuptools wheel > /dev/null 2>&1
python3 setup.py sdist bdist_wheel > /dev/null 2>&1
cp ./dist/MiniPack-0.0.1.tar.gz .
rm -rf MiniPack.egg-info dist build