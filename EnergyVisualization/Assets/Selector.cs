using UnityEngine;

public class Selector : MonoBehaviour
{
    private Camera cam;
    private Building selection;

    private void Awake()
    {
        cam = GetComponent<Camera>();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
            Select();
    }

    private void Select()
    {
        RaycastHit hit;
        Ray ray = cam.ScreenPointToRay(Input.mousePosition);

        if (!Physics.Raycast(ray, out hit) || !hit.transform.TryGetComponent(out Building building))
            return;

        if (building == selection)
        {
            building.Deselect();
            selection = null;
        }
        else
        {
            building.Select();
            selection = building;
        }
    }
}
