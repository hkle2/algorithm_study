
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181878">원하는 문자열 찾기</a></h1><p>알파벳으로 이루어진 문자열 <code>myString</code>과 <code>pat</code>이 주어집니다. <code>myString</code>의 연속된 부분 문자열 중 <code>pat</code>이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.</p>

<p>단, 알파벳 대문자와 소문자는 구분하지 않습니다.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>myString</code>의 길이 ≤ 100,000</li>
<li>1 ≤ <code>pat</code>의 길이 ≤ 300</li>
<li><code>myString</code>과 <code>pat</code>은 모두 알파벳으로 이루어진 문자열입니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>myString</th>
<th>pat</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"AbCdEfG"</td>
<td>"aBc"</td>
<td>1</td>
</tr>
<tr>
<td>"aaAA"</td>
<td>"aaaaa"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>"AbCdEfG"의 0~2번 인덱스의 문자열은 "AbC"이며, 이는 <code>pat</code>인 "aBc"와 같습니다. 따라서 1을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>myString</code>의 길이가 <code>pat</code>보다 더 짧기 때문에 <code>myString</code>의 부분 문자열 중 <code>pat</code>와 같은 문자열이 있을 수 없습니다. 따라서 0을 return 합니다.</li>
</ul>

<p>※2023년 05월 15일 제한사항이 수정되었습니다.</p>

  