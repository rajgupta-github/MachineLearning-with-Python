## ML Deployment

Follow instructions in below article:

https://medium.com/datadriveninvestor/from-model-inception-to-deployment-adce1f5ed9d6

How to run:
1. cd ml_deployment
2. docker-compose up

If you want to test the predict(Post) method, use curl command or use Postman

curl --header "Content-Type: application/json" --request POST --data '[{"sepal_length":6.3,"sepal_width":2.3,"petal_length":4.4,"petal_width":1.3}]' http://localhost:8080/predict