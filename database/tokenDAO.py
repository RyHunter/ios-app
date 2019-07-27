def insertToken(post_id, text, lemma, partOfSpeech, cursor):
    insertQuery = ("INSERT INTO tokens (post_id, text, lemma, part_of_speech) VALUES (%s, %s, %s, %s)")
    tokenData = (post_id, text, lemma, partOfSpeech)
    cursor.execute(insertQuery, tokenData)