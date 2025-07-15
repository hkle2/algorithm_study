
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181842">부분 문자열</a></h1><p>어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열  "abc"는 문자열 "aabcc"의 부분 문자열입니다. </p>

<p>문자열 <code>str1</code>과 <code>str2</code>가 주어질 때, <code>str1</code>이 <code>str2</code>의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.</p>



<h3>제한 사항</h3>

<ul>
<li>1 ≤ <code>str1</code> ≤ <code>str2</code> ≤ 20</li>
<li><code>str1</code>과 <code>str2</code>는 영어 소문자로만 이루어져 있습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>str1</th>
<th>str2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"abc"</td>
<td>"aabcc"</td>
<td>1</td>
</tr>
<tr>
<td>"tbt"</td>
<td>"tbbttb"</td>
<td>0</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>본문과 동일합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"tbbttb"에는 "tbt"가 없으므로 0을 return합니다.</li>
</ul>

  