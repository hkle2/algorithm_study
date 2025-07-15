
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181834">l로 만들기</a></h1><p>알파벳 소문자로 이루어진 문자열 <code>myString</code>이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>myString</code> ≤ 100,000

<ul>
<li><code>myString</code>은 알파벳 소문자로 이루어진 문자열입니다.</li>
</ul></li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>myString</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdevwxyz"</td>
<td>"lllllvwxyz"</td>
</tr>
<tr>
<td>"jjnnllkkmm"</td>
<td>"llnnllllmm"</td>
</tr>
</tbody>
      </table>
<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>0 ~ 4번 인덱스의 문자 "a","b","c","d","e"는 각각 "l"보다 앞서는 문자입니다. 따라서 "l"로 고쳐줍니다.</li>
<li>그 외의 문자는 모두 "l"보다 앞서지 않는 문자입니다. 따라서 바꾸지 않습니다.</li>
<li>따라서 "lllllvwxyz"을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>0번, 1번, 6번, 7번 인덱스의 문자 "j","j","k","k"는 각각 "l"보다 앞서는 문자입니다. 따라서 "l"로 고쳐줍니다.</li>
<li>그 외의 문자는 모두 "l"보다 앞서지 않는 문자입니다. 따라서 바꾸지 않습니다.</li>
<li>따라서 "llnnllllmm"을 return 합니다.</li>
</ul>

  