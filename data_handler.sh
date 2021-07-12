#!/bin/bash


export DATABASE=havacs
export USERNAME=Teszta_123
export HOsTNAME=localhost:5432
export PGPASSWORD=Teszta_123

list_players() {
psql << EOF
SELECT user_name AS "Player name", score AS "Score", difficulty AS Difficulty FROM score
EOF
}

main() {
    if [[ "$1" == "list-players" ]]
    then
        list_players
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]
then
    main "$@"
fi
