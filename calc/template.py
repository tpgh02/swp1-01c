html = b"""
<html>
    <body>
        <form method="get" action="">
            a = <input type="number" name="a" value="%(a)s">
            b = <input type="number" name="b" value="%(b)s"><br><br>

            <input type="submit">
        </form>
	<p>
            sum = %(x)s<br>
	    product = %(y)s
	</p>
    </body>
</html>
"""
