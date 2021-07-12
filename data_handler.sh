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

main() {
    if [[ "$1" == "add-player" ]]
    then
        add_player "$2" "$3" "$4"
    elif [[ "$1" == "list-players" ]]
    then
        list_players
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]
then
    main "$@"
fi
