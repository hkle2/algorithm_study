
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181885">할 일 목록</a></h1><p>오늘 해야 할 일이 담긴 문자열 배열 <code>todo_list</code>와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 <code>finished</code>가 매개변수로 주어질 때, <code>todo_list</code>에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>todo_list</code>의 길이 1 ≤ 100</li>
<li>2 ≤ <code>todo_list</code>의 원소의 길이 ≤ 20

<ul>
<li><code>todo_list</code>의 원소는 영소문자로만 이루어져 있습니다.</li>
<li><code>todo_list</code>의 원소는 모두 서로 다릅니다.</li>
</ul></li>
<li><code>finished[i]</code>는 true 또는 false이고 true는 <code>todo_list[i]</code>를 마쳤음을, false는 아직 마치지 못했음을 나타냅니다.</li>
<li>아직 마치지 못한 일이 적어도 하나 있습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>todo_list</th>
<th>finished</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["problemsolving", "practiceguitar", "swim", "studygraph"]</td>
<td>[true, false, true, false]</td>
<td>["practiceguitar", "studygraph"]</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>todo_list</code> 중에서 "problemsolving"과 "swim"은 마쳤고, "practiceguitar"와 "studygraph"는 아직 마치지 못했으므로 <code>todo_list</code>에서 나온 순서대로 담은 문자열 배열 ["practiceguitar", "studygraph"]를 return 합니다.</li>
</ul>

  