
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181843">부분 문자열인지 확인하기</a></h1><p>부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.</p>

<p>문자열 <code>my_string</code>과 <code>target</code>이 매개변수로 주어질 때, <code>target</code>이 문자열 <code>my_string</code>의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>은 영소문자로만 이루어져 있습니다.</li>
<li>1 ≤ <code>target</code>의 길이 ≤ 100</li>
<li><code>target</code>은 영소문자로만 이루어져 있습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>target</th>
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
<td>"wxyz"</td>
<td>0</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>문제 설명과 같습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>문제 설명과 같습니다.</li>
</ul>

  