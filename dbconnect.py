import psycopg2.extras

DB_HOST = ""
DB_NAME = ""
DB_USER = ""
DB_PASS = ""


def getAllRowsWithMachingBranches(query, limit, offset=0):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM public.bank_branches WHERE branch ilike '{0}%' ORDER BY ifsc ASC LIMIT {1}"
                        " OFFSET {2} ROWS;".format(query, limit, offset))
            data = cur.fetchall()

            branches = {"branches": []}
            for branch in data:
                branches['branches'].append({
                    'ifsc': branch[0],
                    'bank_id': branch[1],
                    'branch': branch[2],
                    'address': branch[3],
                    'city': branch[4],
                    'district': branch[5],
                    'state': branch[6],
                    'bank_name': branch[7]
                })

            return branches


def getAllRowsWithMachingQuery(query, limit, offset=0):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cs = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name']
            data = []
            for c in cs:
                cur.execute("SELECT * FROM public.bank_branches WHERE {0} ilike '{1}%' ORDER BY ifsc ASC LIMIT {2}"
                            " OFFSET {3} ROWS;".format(c, query, limit, offset))
                part = cur.fetchall()

                for l in part:
                    ifsc = l[0]
                    present = False
                    for br in data:
                        if br[0] == ifsc:
                            present = True
                            break
                    if not present:
                        data.append(l)

            branches = {"branches": []}
            for branch in data:
                branches['branches'].append({
                    'ifsc': branch[0],
                    'bank_id': branch[1],
                    'branch': branch[2],
                    'address': branch[3],
                    'city': branch[4],
                    'district': branch[5],
                    'state': branch[6],
                    'bank_name': branch[7]
                })

            return branches


