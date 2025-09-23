BASE_URL="http://localhost:8000/tasks"

curl -X POST \
  $BASE_URL \
  -H 'Content-Type: application/json' \
  -d '{"title": "Первая задача", "is_completed": false}'

curl -X POST \
  $BASE_URL \
  -H 'Content-Type: application/json' \
  -d '{"title": "Вторая задача", "is_completed": false}'


curl -s -X GET $BASE_URL | jq .

curl -X DELETE \
  $BASE_URL/1 \

curl -X PUT \
  $BASE_URL/2 \
  -H 'Content-Type: application/json' \
  -d '{"title": "Первая задача", "is_completed": false}'

curl -X POST \
  $BASE_URL \
  -H 'Content-Type: application/json' \
  -d '{"title": "Вторая задача", "is_completed": false}'

curl -X PATCH \
  $BASE_URL/3 \
  -H 'Content-Type: application/json' \
  -d '{"is_completed": true}'


curl -s -X GET $BASE_URL | jq .