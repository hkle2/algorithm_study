
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181867">x 사이의 개수</a></h1><p>문자열 <code>myString</code>이 주어집니다. <code>myString</code>을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>myString</code>의 길이 ≤ 100,000

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
<td>"oxooxoxxox"</td>
<td>[1, 2, 1, 0, 1, 0]</td>
</tr>
<tr>
<td>"xabcxdefxghi"</td>
<td>[0, 3, 3, 3]</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>"x"를 기준으로 문자열을 나누면 ["o", "oo", "o", "", "o", ""]가 됩니다. 각각의 길이로 배열을 만들면 [1, 2, 1, 0, 1, 0]입니다. 따라서 [1, 2, 1, 0, 1, 0]을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"x"를 기준으로 문자열을 나누면 ["", "abc", "def", "ghi"]가 됩니다. 각각의 길이로 배열을 만들면 [0, 3, 3, 3]입니다. 따라서 [0, 3, 3, 3]을 return 합니다.</li>
</ul>

  