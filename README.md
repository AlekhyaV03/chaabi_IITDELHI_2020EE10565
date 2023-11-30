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
some sample outputs
