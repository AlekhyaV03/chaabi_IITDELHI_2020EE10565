# chaabi_IITDELHI_2020EE10565
Instructions for running the code:
first you have to download docker from:
https://www.docker.com/products/docker-desktop/
then you have to connect to docker server by running the following command in the terminal
docker run -p 6333:6333 qdrant/qdrant
after this you have to run the file with name "vector_embedding.py" by typing the following in the cmd. This may take some time(around 10minutes)
python vector_embedding.py 
then run "app.py" file by running the following command in the terminal(do this in another terminal)
python app.py
then type your query in the terminal
Important:during the entire process docker should be running in the port 6333 in a terminal in the background
some sample outputs:
Example-1:Query = " Suggest healthy snacks"
          Output:
          1. Yoghurt Berry + Anti-Oxidants: This balanced snack is gluten-free, rich in fiber, rich in protein, and contains no preservatives. It is also a good source of energy.
          2. Nutty Apricot + Fibre: Another balanced snack option that is gluten-free, rich in fiber, rich in protein, and contains no preservatives. It is also a good source of energy.
Example-2:Query = "Suggest ayurvedic hair products" 
          Output:
          Here are some suggestions for ayurvedic hair products:
          1. Hair Oil - Ayurvedic Care: This oil improves hair growth, prevents hair loss and premature greying of hair, and fights against dandruff. For more beauty tips and tricks, visit [https://bigbasket.blog/](https://bigbasket.blog/).
          2. Hair Oil - Anti-Hair Fall: This bottle contains a whole bunch of ayurvedic ingredients like Rosemary, Coriander, and Palma Rosa. It acts deep within the scalp to reduce hair fall. It also fights dandruff, greying, and split              ends. Add a little ayurvedic care to increase overall hair health and make heads turn. For more beauty tips and tricks, visit [http://lookbeautiful.in/](http://lookbeautiful.in/) or [https://bigbasket.blog/]          
          (https://bigbasket.blog/).

          
