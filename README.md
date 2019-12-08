# Machine Learning With Python


## How to Automatically Import Your Favorite Libraries into IPython or a Jupyter Notebook

1. Navigate to ~/.ipython/profile_default
2. Create a folder called startup if it’s not already there
3. Add a new Python file called start.py
4. Put your favorite imports in this file (Refer https://github.com/rajgupta-github/MachineLearning-with-Python/blob/master/jupyter_notebook_template/)
5. Launch IPython or a Jupyter Notebook and your favorite libraries will be automatically loaded every time!

## Useful Commands

1. jupyter notebook
2. ipython
3. pip install <package_name>
4. pip3.7 freeze
5. lsof -i :<port>
6. kill -9 <pid>
7. python3.7 app.py
8. ssh-keygen -t rsa -C "rajkumargupta1@gmail.com" -f '/Users/rajkgupta/.ssh/id_rsa_personal'

## ML Deployment

Follow instructions in below article
https://medium.com/datadriveninvestor/from-model-inception-to-deployment-adce1f5ed9d6

How to run:
cd ml_deployment
docker-compose up

If you want to test the predict(Post) method, use curl command or use Postman
curl --header "Content-Type: application/json" --request POST --data '[{"sepal_length":6.3,"sepal_width":2.3,"petal_length":4.4,"petal_width":1.3}]' http://localhost:8080/predict