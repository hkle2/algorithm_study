
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181908">접미사인지 확인하기</a></h1><p>어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.<br>
문자열 <code>my_string</code>과 <code>is_suffix</code>가 주어질 때, <code>is_suffix</code>가 <code>my_string</code>의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>is_suffix</code>의 길이 ≤ 100</li>
<li><code>my_string</code>과 <code>is_suffix</code>는 영소문자로만 이루어져 있습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>is_suffix</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"banana"</td>
<td>"ana"</td>
<td>1</td>
</tr>
<tr>
<td>"banana"</td>
<td>"nan"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"wxyz"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"abanana"</td>
<td>0</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사이기 때문에 1을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>예제 3번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>예제 4번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

  