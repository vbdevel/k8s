# Преобразуем base64url в base64
base64_payload=$(echo "eyJpc3MiOiJodHRwczovL2Rldi0xNzZobDFtemZ3ODEzOHNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiI5bDBuMEQ2czBqbDE0WnY0Qmg1ZW1uY3BqVk5aRWhKQUBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9maXJzdC53ZGIuY29tLnVhIiwiaWF0IjoxNzE1OTc1NDY5LCJleHAiOjE3MTYwNjE4NjksImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IjlsMG4wRDZzMGpsMTRadjRCaDVlbW5jcGpWTlpFaEpBIn0" | tr '_-' '/+')

# Добавляем padding, чтобы длина была кратной 4
padding=$(echo $(( 4 - (${#base64_payload} % 4) )))
if [ $padding -lt 4 ]; then
  base64_payload="$base64_payload$(printf '%.0s=' $(seq 1 $padding))"
fi

# Декодируем base64
echo $base64_payload | base64 --decode

