#!/bin/bash


export DATABASE=havacs
export USERNAME=Teszta_123
export HOsTNAME=localhost:5432
export PGPASSWORD=Teszta_123

add_player() {
psql <<EOF
INSERT INTO score (user_name, score, difficulty)
VALUES ('$1', '$2', '$3')
EOF
}

list_players() {
psql << EOF
SELECT user_name AS "Player name", score AS "Score", difficulty AS Difficulty FROM score
EOF
}

list_best_players_by_difficulty() {
psql << EOF
SELECT user_name AS "Player name", score AS "Score", difficulty AS Difficulty FROM score
WHERE difficulty = '$@'
ORDER BY score DESC
LIMIT 10
EOF
}

list_players_by_name() {
psql << EOF
SELECT user_name AS "Player name", score AS "Score", difficulty AS Difficulty FROM score
WHERE user_name = '$@'
GROUP BY difficulty, score, user_name
ORDER BY difficulty, score DESC
EOF
}

main() {
    if [[ "$1" == "add-player" ]]
    then
        add_player "$2" "$3" "$4"
    elif [[ "$1" == "list-players" ]]
    then
        list_players
    elif [[ "$1" == "list-best-players-by-difficulty" ]]
    then
        list_best_players_by_difficulty "$2"
    elif [[ "$1" == "list-players-by-name" ]]
    then
        list_players_by_name "$2"
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]
then
    main "$@"
fi
