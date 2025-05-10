
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/120821">배열 뒤집기</a></h1><p>정수가 들어 있는 배열 <code>num_list</code>가 매개변수로 주어집니다. <code>num_list</code>의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>num_list</code>의 길이 ≤ 1,000</li>
<li>0 ≤ <code>num_list</code>의 원소 ≤ 1,000</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>[5, 4, 3, 2, 1]</td>
</tr>
<tr>
<td>[1, 1, 1, 1, 1, 2]</td>
<td>[2, 1, 1, 1, 1, 1]</td>
</tr>
<tr>
<td>[1, 0, 1, 1, 1, 3, 5]</td>
<td>[5, 3, 1, 1, 1, 0, 1]</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li><code>num_list</code>가 [1, 2, 3, 4, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 4, 3, 2, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num_list</code>가 [1, 1, 1, 1, 1, 2]이므로 순서를 거꾸로 뒤집은 배열 [2, 1, 1, 1, 1, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><code>num_list</code>가 [1, 0, 1, 1, 1, 3, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 3, 1, 1, 1, 0, 1]을 return합니다.</li>
</ul>

  