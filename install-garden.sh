#!/usr/bin/env bash
tar -xzf Garden-of-Freedom-v1.0.tar.gz -C ~/
sudo ln -sf ~/.garden/lantern/garden_lantern.sh /usr/local/bin/garden
chmod +x ~/.garden/lantern/garden_lantern.sh ~/.garden/lantern/commands/*
echo "Garden installed."
