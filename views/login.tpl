%include('header')
<form action="/login" method="POST">
    <input type="text" name="USER" placeholder="USER" required>
    <input type="password" name="PASS" placeholder="PASSWORD" required>
    <button type="submit">GO</button>
</form>
%include('footer')