
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181883">수열과 구간 쿼리 1</a></h1><p>정수 배열 <code>arr</code>와 2차원 정수 배열 <code>queries</code>이 주어집니다. <code>queries</code>의 원소는 각각 하나의 <code>query</code>를 나타내며, <code>[s, e]</code> 꼴입니다.</p>

<p>각 <code>query</code>마다 순서대로 <code>s</code> ≤ <code>i</code> ≤ <code>e</code>인 모든 <code>i</code>에 대해 <code>arr[i]</code>에 1을 더합니다.</p>

<p>위 규칙에 따라 <code>queries</code>를 처리한 이후의 <code>arr</code>를 return 하는 solution 함수를 완성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 1,000

<ul>
<li>0 ≤ <code>arr</code>의 원소 ≤ 1,000,000</li>
</ul></li>
<li>1 ≤ <code>queries</code>의 길이 ≤ 1,000

<ul>
<li>0 ≤ <code>s</code> ≤ <code>e</code> &lt; <code>arr</code>의 길이</li>
</ul></li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>queries</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[0, 1, 2, 3, 4]</td>
<td>[[0, 1],[1, 2],[2, 3]]</td>
<td>[1, 3, 4, 4, 4]</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>각 쿼리에 따라 <code>arr</code>가 다음과 같이 변합니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>i</th>
<th>queries[i]</th>
<th>arr</th>
</tr>
</thead>
        <tbody><tr>
<td>-</td>
<td>-</td>
<td>[0, 1, 2, 3, 4]</td>
</tr>
<tr>
<td>0</td>
<td>[0,1]</td>
<td>[1, 2, 2, 3, 4]</td>
</tr>
<tr>
<td>1</td>
<td>[1,2]</td>
<td>[1, 3, 3, 3, 4]</td>
</tr>
<tr>
<td>2</td>
<td>[2,3]</td>
<td>[1, 3, 4, 4, 4]</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서 [1, 3, 4, 4, 4]를 return 합니다.</li>
</ul>

  