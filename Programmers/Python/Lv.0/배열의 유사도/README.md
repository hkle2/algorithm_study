
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/120903">배열의 유사도</a></h1><p>두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 <code>s1</code>과 <code>s2</code>가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 원소의 길이 ≤ 10</li>
<li><code>s1</code>과 <code>s2</code>의 원소는 알파벳 소문자로만 이루어져 있습니다</li>
<li><code>s1</code>과 <code>s2</code>는 각각 중복된 원소를 갖지 않습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>s1</th>
<th>s2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a", "b", "c"]</td>
<td>["com", "b", "d", "p", "c"]</td>
<td>2</td>
</tr>
<tr>
<td>["n", "omg"]</td>
<td>["m", "dot"]</td>
<td>0</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>"b"와 "c"가 같으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>같은 원소가 없으므로 0을 return합니다.</li>
</ul>

  