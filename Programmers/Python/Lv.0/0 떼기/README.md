
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181847">0 떼기</a></h1><p>정수로 이루어진 문자열 <code>n_str</code>이 주어질 때, <code>n_str</code>의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.</p>



<h3>제한사항</h3>

<ul>
<li>2 ≤ <code>n_str</code> ≤ 10</li>
<li><code>n_str</code>이 "0"으로만 이루어진 경우는 없습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>n_str</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"0010"</td>
<td>"10"</td>
</tr>
<tr>
<td>"854020"</td>
<td>"854020"</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>"0010"의 가장 왼쪽에 연속으로 등장하는 "0"을 모두 제거하면 "10"이 됩니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"854020"는 가장 왼쪽에 0이 없으므로 "854020"을 return합니다.</li>
</ul>

  