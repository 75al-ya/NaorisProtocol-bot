<<<<<<< HEAD
#!/bin/bash

echo "Bot Launcher"

if [ -f "requirements.txt" ]; then
    echo "Installing wheel for faster installation..."
    pip install wheel
    
    echo "Installing requests..."
    pip install requests
    
    echo "Installing dependencies..."
    pip install -r requirements.txt
    
    echo ""
    echo "Starting the bot..."
    python bot.py
else
    echo "requirements.txt not found, skipping dependency installation."
fi

=======
#!/bin/bash

echo "Bot Launcher"

if [ -f "requirements.txt" ]; then
    echo "Installing wheel for faster installation..."
    pip install wheel
    
    echo "Installing requests..."
    pip install requests
    
    echo "Installing dependencies..."
    pip install -r requirements.txt
    
    echo ""
    echo "Starting the bot..."
    python bot.py
else
    echo "requirements.txt not found, skipping dependency installation."
fi

>>>>>>> 6dec1e80d791f1176e43ec946037c4b17ddbc34c
echo "failed"