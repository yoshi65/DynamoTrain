# DynamoTrain

## SETTING
1. dockerのインストール
1. python3.6のインストール
1. pipのインストール
1. aws-sam-cliのインストール
    ```sh
    % pip install awscli aws-sam-cli
    ```
1. awsの初期設定
    ```sh
    % aws configure
    AWS Access Key ID: 
    AWS Secret Access Key:
    Default region name: ap-northeast-1
    Default output format:
    ```

## How to test local
1. start DynamoDB local
    ```sh
    % docker run -d -p 8000:8000 --hostname DynamoTrain --name DynamoTrain amazon/dynamodb-local
    ```
1. get DynamoDB IP address
    ```sh
    % docker ps | awk 'NR>1&&$0=$1' | xargs -n 1 docker inspect -f "{{.Name}} {{.NetworkSettings.IPAddress }}"
    ```
1. create tables
    ```sh
    % python create_table.py
    ```
1. test post and get
    ```sh
    % curl -XPOST -d '{"vote": "tabs"}' http://127.0.0.1:3000/dynamotrain
    % curl -XGET -d '{"vote": "tabs"}' http://127.0.0.1:3000/dynamotrain
    ```

## References
* https://blue21neo.blogspot.com/2018/02/aws-sam-local-dynamodb-local-api.html
