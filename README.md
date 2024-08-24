# Vainos Template
 Vainos template is a easy to start template for Bootstrap+Flask development. 

 # Folder Structure
 templates
    |__Modules - Reusable modules for pages
    |__Pages

 assets
    |_images -- image files
    ... any other assets

requirements.txt
    |_Insert all your python PIP required packages here so others can install it quickly using 
    pip install -r requirements.txt

     # Set Up

     To use the Vainos template for your Bootstrap+Flask development, follow these steps:

     1. Clone the repository to your local machine:
     2. Navigate to the project directory:
        ```
        cd vainos-template
        ```
     2.5 [Optional] Start a virtual environment:
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```

     3. Install the required dependencies:
        ```
        pip install -r requirements.txt
        ```

     4. Start the Flask development server:

        If running from Mac/Linux, make sure that the sh file has permission to execute.
        ```
        chmod +x run_mac.sh
        ```

        Run wither run_mac or run_win based on your system. Linux users should use run_mac.
        ```
        ./run_mac.sh
        {Mac}
        or
        run_win.bat 
        {Windows}
        ```

     5. Open your web browser and visit `http://localhost:5000` to see the template in action.

     # Customization

     The Vainos template is highly customizable. Here are a few ways you can customize it to fit your needs:

     - Modify the existing modules in the `templates/Modules` directory or create new ones.
     - Add your own pages in the `templates/Pages` directory.
     - Update the styles and layout by modifying the CSS files in the `assets/css` directory.
     - Replace the default images in the `assets/images` directory with your own.

     Feel free to explore the template and make it your own!

     # Contributing

     If you find any issues or have suggestions for improvements, please feel free to contribute to the Vainos template by submitting a pull request. We welcome any contributions that can make the template better.

     # License

     The Vainos template is developed by Dr Ivan Ling from University of Southampton. Please give attribution if used.


